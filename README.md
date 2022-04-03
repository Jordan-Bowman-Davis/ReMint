# ReMint
ReMint is an proof of concept that demos how an NFT can be broken down into component pieces. 
Future iterations will allow user's to "ReMint" their NFTs from these components, and even exchange their ReMint-ed version for the original.

ReMint takes an NFT, created by the MyNFT.sol contract, and locks it into the NftExchange.sol contract. NftExchange.sol then releases components to the calling 
address if the caller owns the NFT dictated by the tokenID.

As of now, the mapping from original NFT to components is done on-chain, but future iterations shall use a metadata standard that includes component info and images.

### MyNFT.sol functions 
<code>function mintNFT(address recipient, string memory tokenURI) public onlyOwner returns (uint256)</code>

### NftExchange.sol functions 
<code>function exchangeNFT(uint256 tokenId) public returns (uint256, uint256, uint256, uint256)</code>

<code>function mintNFT(address recipient, string[] memory tokenURI) private onlyOwner returns (uint256, uint256, uint256, uint256)</code>
