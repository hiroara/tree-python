const gulp = require('gulp')
const concat = require('gulp-concat')
const shell = require('gulp-shell')

const src = {
  lib: 'tree/**/*.py',
  test: 'tests/**/*.py',
}

gulp.task('test', () => gulp
  .src([src.lib, src.test])
  .pipe(concat('all.py'))
  .pipe(shell('env/bin/python setup.py test'))
)

gulp.task('watch', () => gulp.watch([src.lib, src.test], ['test']))

gulp.task('default', ['test', 'watch'])
