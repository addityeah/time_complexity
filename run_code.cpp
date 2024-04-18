#include <iostream>
#include <vector>
#include <stdexcept> 
#include "L5_Q1.cpp"  // implementation file

int main(int argc, char* argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: program input_data" << std::endl;
        return 1;
    }

    std::vector<int> data;
    try {
        for (int i = 1; i < argc; ++i) {
            int value = std::stoi(argv[i]);
            data.push_back(value);
        }
    } catch (const std::invalid_argument& e) {
        std::cerr << "Invalid argument: " << e.what() << std::endl;
        return 1;
    } catch (const std::out_of_range& e) {
        std::cerr << "Out of range error: " << e.what() << std::endl;
        return 1;
    }

    Solution solution;  
    int count = solution.threeSum(data);  // threeSum call
    std::cout << "Result: " << count << std::endl;
    return 0;
}
