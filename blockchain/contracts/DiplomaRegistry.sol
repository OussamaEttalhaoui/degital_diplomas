// contracts/DiplomaRegistry.sol
pragma solidity ^0.8.0;

contract DiplomaRegistry {
    struct Diploma {
        string name;
        string firstName;
        string cne;
        string cin;
        string degree;
        string specialization;
        string university;
        uint256 year;
        string mention;  
    }

    mapping(address => Diploma) public diplomas;

    function registerDiploma(
        string memory name,
        string memory firstName,
        string memory cne,
        string memory cin,
        string memory degree,
        string memory specialization,
        string memory university,
        uint256 year,
        string memory mention 
    ) public {
        diplomas[msg.sender] = Diploma(name, firstName, cne, cin, degree, specialization, university, year, mention);
    }

    function getDiploma(address student) public view returns (Diploma memory) {
        return diplomas[student];
    }
}
