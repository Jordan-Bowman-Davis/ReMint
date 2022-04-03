async function main() {
    const NftExchange = await ethers.getContractFactory("NftExchange")
  
    // Start deployment, returning a promise that resolves to a contract object
    const NftExchange = await NftExchange.deploy()
    await NftExchange.deployed()
    console.log("Contract deployed to address:", NftExchange.address)
  }
  
  main()
    .then(() => process.exit(0))
    .catch((error) => {
      console.error(error)
      process.exit(1)
    })
  