const { defineConfig } = require('cypress')

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
    defaultCommandTimeout: 1000,
    supportFile: false,
    specPattern: '/cypress/e2e/**/*.cy.{js,jsx,ts,tsx}',
    reporter: 'junit',
    reporterOptions: {
      mochaFile: '/results/cypress_result.xml',
      toConsole: false
    }
  }
}) 