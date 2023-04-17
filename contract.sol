<<<<<<< HEAD
pragma solidity ^0.6.0;

contract PrivateData{
    uint numberParents = 0;
    uint numberPatients = 0;
    struct Patient{
        uint id;
        string name;
        string familyName;
        string birthdate;
    }
    struct Parent{
        address id;
        string name;
        string familyName;
        string email;
        string telephone;
        string password;
        uint numberPatients;
        mapping(uint => uint) patients;
    }
    mapping(address => uint) parents;

    function public getParent(address _id) view returns (Parent){
        for(uint i=0; i < numberParents; i++){
            if(parents[i].id == _id){
                return parents[i];
            }
        }
        return null;
    }

    function public createParent(struct Parent memory parent){
        parents[numberParents] = parent;
        numberParents++;
    }
    constructor public(){

    }
=======
pragma solidity ^0.8;
contract PrivateData{
    uint256 numberPatients = 0;
    struct Patient{
        uint256 id;
        string name;
        string familyName;
        string birthdate;
        string school;
        uint256 parentId;
    }
    mapping(uint256 => Patient) public patients;
    uint256[] public patientsIds;


    function  createPatient(uint256 id, string memory name, string memory familyName, string memory birthdate,
        string memory school, uint256 parentId) public{
        patients[id] = Patient(id, name, familyName, birthdate, school, parentId);
        patientsIds.push(id);
    }

    function getPatientById(uint256 id) public view returns(Patient memory){
        return patients[id];
    }

    function deletePatient(uint256 id) public returns (bool){
        delete patients[id];
        for(uint256 i = 0; i < numberPatients; i++){
            if(patientsIds[i] == id){
                patientsIds[i] = patientsIds[patientsIds.length -1];
                delete patientsIds[patientsIds.length - 1];
                return true;
            }
        }
        return false;
    }


    function updatePatient(uint256 id, string memory name, string memory familyName, string memory birthdate,
        string memory school) public{
        Patient memory patient = patients[id];
        patient.name = name;
        patient.familyName = familyName;
        patient.birthdate = birthdate;
        patient.school = school;
        patients[id] = patient;
    }


>>>>>>> origin/main
}
