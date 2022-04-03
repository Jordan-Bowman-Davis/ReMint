//Contract based on [https://docs.openzeppelin.com/contracts/3.x/erc721](https://docs.openzeppelin.com/contracts/3.x/erc721)
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract NftExchange is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    constructor() ERC721("NftExchange", "NFT") {}

    function exchangeNFT(uint256 tokenId) public returns (uint256, uint256, uint256, uint256)
    {
        address owner = _msgSender();
        // mapping that establishes components given out for each object
        mapping(uint256 => string[]) components;
        components[3] = ["ipfs://QmVJwF2w4A7PcsKqhGpxPJnPQJGofnoZUDDvjh3dDZ1TrT", "ipfs://QmQBxvkXDqSRTQNh1AFZGUCcCNwHYWHrQ7yE6YgKHYQix6", "ipfs://QmdVenFJTjBNtDyQThzcsdQf9kSGBpNKWHbVJJ3dP7HP9e", "ipfs://QmYKweJkqnrS4nLS9ToSX7xPYzu2LhquPctoyoEVFzbuHD"];

        // checks to see owner's NFT is in database
        require(tokenId == 4, "Sender not authorized.");
        
        // transfers owner's NFT to contract address
        transferFrom(owner, address(this), tokenId);

        // mints component NFTs based on submitted NFT ID
        return mintNFT(owner, components[3]);
    }

    // mints components based on mapping provided
    function mintNFT(address recipient, string[] memory tokenURI) private onlyOwner returns (uint256, uint256, uint256, uint256) 
    {
        _tokenIds.increment();
        uint256 newItemId1 = _tokenIds.current();
        _mint(recipient, newItemId1);
        _setTokenURI(newItemId1, tokenURI[0]);
        _tokenIds.increment();

        uint256 newItemId2 = _tokenIds.current();
        _mint(recipient, newItemId2);
        _setTokenURI(newItemId2, tokenURI[1]);
        _tokenIds.increment();

        uint256 newItemId3 = _tokenIds.current();
        _mint(recipient, newItemId3);
        _setTokenURI(newItemId3, tokenURI[2]);
        _tokenIds.increment();

        uint256 newItemId4 = _tokenIds.current();
        _mint(recipient, newItemId4);
        _setTokenURI(newItemId4, tokenURI[3]);

        return (newItemId1, newItemId2, newItemId3, newItemId4);
    }

}
