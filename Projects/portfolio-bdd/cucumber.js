
module.exports = {
  default: {
    paths: ['features/**/*.feature'],
    require: [
      'features/step-definitions/*.js',
      'support/*.js'
    ],
    format: [
      'progress',
      'html:reports/cucumber-report.html'
    ],
    publishQuiet: true
  }
};
