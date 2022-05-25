module.exports = {
  publicPath:
    process.env.NODE_ENV === "production"
      ? "./dist/"
      : process.env.BASE_URL || "http://localhost:8080",
  outputDir: "./dist",
  indexPath: "./public/index.html",

  chainWebpack: (config) => {
    config.devServer
      .public("http://localhost:8080")
      .hotOnly(true)
      .headers({ "Access-Control-Allow-Origin": "*" })
      .writeToDisk((filePath) => filePath.endsWith("index.html"));
  },
};
