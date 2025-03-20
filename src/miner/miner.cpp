#include <iostream>
#include "randomx.hpp"
#include "blockchain.hpp" // Aqui deve estar a interface para a blockchain da LibertCoin

int main() {
    std::cout << "Iniciando a mineração da LibertCoin Quantum..." << std::endl;

    // Configurar o algoritmo RandomX
    RandomX miner;
    miner.setCacheSize(2); // Ajuste o tamanho do cache de acordo com o seu dispositivo
    miner.setThreads(4);   // Ajuste conforme o número de núcleos do seu dispositivo

    while (true) {
        miner.mineBlock(); // Minerando um novo bloco
        if (miner.isBlockValid()) {
            std::cout << "Bloco minerado com sucesso!" << std::endl;
            // Enviar o bloco para a blockchain da LibertCoin
            Blockchain blockchain;
            blockchain.submitBlock(miner.getBlock());
        } else {
            std::cout << "Falha na mineração. Tentando novamente..." << std::endl;
        }
    }

    return 0;
}
