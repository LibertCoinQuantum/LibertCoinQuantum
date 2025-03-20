#include "blockchain.hpp"

Blockchain::Blockchain() {
    // Inicializa a blockchain com um bloco gênese (bloco inicial)
    chain.push_back("Bloco Gênese");
}

void Blockchain::submitBlock(const std::string& block) {
    // Simulando o envio do bloco para a rede
    if (validateBlock(block)) {
        chain.push_back(block);
        std::cout << "Bloco " << block << " adicionado à blockchain." << std::endl;
    } else {
        std::cout << "Bloco " << block << " é inválido!" << std::endl;
    }
}

bool Blockchain::validateBlock(const std::string& block) {
    // Realiza uma validação simples (exemplo)
    // Aqui você pode colocar a lógica para validar o bloco minerado
    return true;  // Em uma rede real, você validaria o bloco de acordo com regras da blockchain
}
