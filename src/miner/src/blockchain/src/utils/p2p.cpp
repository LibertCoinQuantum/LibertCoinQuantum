#include <iostream>
#include <boost/asio.hpp>

class P2P {
public:
    void startServer() {
        boost::asio::io_service io_service;
        boost::asio::ip::tcp::endpoint endpoint(boost::asio::ip::tcp::v4(), 12345);
        boost::asio::ip::tcp::acceptor acceptor(io_service, endpoint);
        boost::asio::ip::tcp::socket socket(io_service);

        acceptor.accept(socket);
        std::cout << "Conexão P2P estabelecida!" << std::endl;

        // Aqui, você pode enviar ou receber blocos entre nós
        // Exemplo de recebimento:
        std::string msg = "Bloco minerado";
        boost::asio::write(socket, boost::asio::buffer(msg));
    }
};
