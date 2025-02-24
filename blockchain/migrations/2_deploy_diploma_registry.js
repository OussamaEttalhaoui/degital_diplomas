const DiplomaRegistry = artifacts.require("DiplomaRegistry");

module.exports = async function (deployer) {
  await deployer.deploy(DiplomaRegistry);
};

