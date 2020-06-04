module.exports = {
  pluginOptions: {
    "style-resources-loader": {
      preProcessor: "scss",
      patterns: [],
    },
    storybook: {
      allowedPlugins: ["style-resources-loader"],
    },
  },
};
