const path = require('path')

module.exports = {
  publicPath: '/static/frontend/',
  outputDir: path.resolve(__dirname, '../static/frontend'),
  assetsDir: 'assets',
  indexPath: path.resolve(__dirname, '../templates/frontend/app.html'),
  productionSourceMap: false,
  configureWebpack: {
    resolve: {
      fallback: {
        path: require.resolve('path-browserify')
      }
    }
  },
  devServer: {
    proxy: {
      '^/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true
      },
      '^/subscription': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true
      },
      '^/$': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true
      }
    }
  }
}
