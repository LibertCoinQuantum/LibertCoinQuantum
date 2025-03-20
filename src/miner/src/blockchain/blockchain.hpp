#ifndef BLOCKCHAIN_HPP
#define BLOCKCHAIN_HPP

#include <vector>
#include <iostream>

class Blockchain {
public:
    Blockchain();
    void submitBlock(const std::string& block);  // Método para submeter bloco minerado
    bool validateBlock(const std::string& block); // Método para validar um bloco

private:
    std::vector<std::string> chain;  // A cadeia de blocos
};

#endif
