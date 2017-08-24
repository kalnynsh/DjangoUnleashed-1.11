var gulp = require('gulp');
var sass = require('gulp-sass');
var cleanCSS = require('gulp-clean-css')
var autoprefixer = require('gulp-autoprefixer');
var plumber = require('gulp-plumber');
var del = require('del');
var rename  = require('gulp-rename');
var sourcemaps = require('gulp-sourcemaps');
var imagemin = require('gulp-imagemin')
var concat  = require('gulp-concat');
var uglify = require('gulp-uglify');
var gutil = require('gulp-util');

var bowserSync = require('browser-sync').create();
var reload = bowserSync.reload;

var paths = {
    html: ['./templates/**/*.html'],
    sass: ['./resource/scss/**/*.scss'],
    css: ['./static/css'],
    js_src: ['./resource/js'],
    js_libs: ['./resource/libs'],
    js_dest: ['./static/js'],
    build: ['./build'],
    img: ['./resource/img'],
    fonts: ['./resource/fonts'],
    src: ['./']
};

// HTML
gulp.task('html', function() {
    gulp.src(paths.html)
    .pipe(reload({stream: true}));
});

// Sass, minify css
gulp.task('styles', function() {
    return gulp.src(paths.sass)
        .pipe(sourcemaps.init())
        .pipe(sass().on('error', notify.onError()))
        .pipe(autoprefixer('last 3 versions'))
        .pipe(cleanCSS())
        .pipe(rename({suffix: '.min', prefix : ''}))
        .pipe(sourcemaps.write())
        .pipe(gulp.dest(''+paths.css+''))
        .pipe(reload({stream: true}));
});

// Java script
gulp.task('common-js', function() {
	return gulp.src([
		paths.js_src,
	])
	.pipe(concat('common.min.js'))
	.pipe(uglify())
	.pipe(gulp.dest(paths.js_src));
});

gulp.task('js', ['common-js'], function() {
	return gulp.src([
	    '/resource/libs/jquery/dist/jquery.min.js',
		'/resource/libs/popper/popper.min.js',
		'/resource/libs/bootstrap/js/dist/bootstrap.min.js',
		'/resource/js/common.min.js', // Всегда в конце
		])
	.pipe(concat('scripts.min.js'))
	//.pipe(uglify()) // Минимизировать весь js (на выбор)
	.pipe(gulp.dest(paths.js_dest))
	.pipe(reload({stream: true}));
});


// bowserSyn, static server
gulp.task('bowserSync', function() {

	bowserSync.init({
	     server: {
		    baseDir: paths.src                
		},
		port: 3000,
		open: true,
		notify: false,
	});
});

// Watch on 
gulp.task('watcher',function() {
    gulp.watch(paths.sass, ['styles']);
    gulp.watch(paths.js_src, paths.js_libs, ['js']);
    gulp.watch(paths.html, ['html']);
});

// Image min
gulp.task('imagemin', function() {
	return gulp.src(paths.img+'/**/*')
	.pipe(cache(imagemin()))
	.pipe(gulp.dest(paths.build+'/img')); 
});


// Задачи сборки
// Создание папки build, очистка неиспользуемых файлов и папок
// Create
gulp.task('build', ['clean', 'imagemin', 'styles', 'js'], function() {

	var buildFiles = gulp.src([
		    paths.html,
		]).pipe(gulp.dest(paths.build));

	var buildCss = gulp.src([
		paths.css+'/main.min.css',
		]).pipe(gulp.dest(paths.build + '/css'));

	var buildJs = gulp.src([
		paths.js_dest + '/scripts.min.js',
		]).pipe(gulp.dest(paths.build + '/js'));

	var buildFonts = gulp.src([
		    paths.fonts+'/**/*',
		]).pipe(gulp.dest(paths.build + '/fonts'));

});

gulp.task('clean', function() { return del.sync('build'); });
gulp.task('clearcache', function () { return cache.clearAll(); });


gulp.task('default', ['watcher', 'styles', 'bowserSync', 'html', 'js']);
