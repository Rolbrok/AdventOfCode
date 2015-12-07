///////////////////////////////////////////////////////////////////////////////
//  filename: puzzle1.cpp
//
//  author:   bdefrance
//  date:     Mon 07 Dec 2015
///////////////////////////////////////////////////////////////////////////////

#include <iostream>
#include <string>
#include <map>
#include <algorithm>
#include <vector>
#include <sstream>
#include <stdlib.h>

std::vector<std::string> &split(const std::string &s, 
                                char delim, 
                                std::vector<std::string> &elems) {
    std::stringstream ss(s);
    std::string item;
    while (std::getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}

bool is_number(const std::string& s)
{
    std::string::const_iterator it = s.begin();
    while (it != s.end() && std::isdigit(*it)) ++it;
    return !s.empty() && it == s.end();
}

int main(int argc, char *argv[])
{
    std::map<std::string, unsigned short> signals;
    std::vector< std::vector<std::string> > lines;
    std::string buf;
    size_t size = 0;    

    while (std::getline(std::cin, buf)) {
        std::vector<std::string> b;
        b = split(buf, ' ', b);
        lines.push_back(b);
        size++;
    }

    for (size_t i = 0; i < 100000; i++) {
        std::vector<std::string> cur_line = lines[i % lines.size()];
        size_t cur_size = cur_line.size();

        std::string dest = cur_line[cur_size - 1];
        cur_size -= 2;
        unsigned short m_buf;
        if (cur_size == 1) {
            if (is_number(cur_line[0])) {
                m_buf = ( atoi(cur_line[0].c_str()) );
            } else if (signals.find(cur_line[0]) != signals.end()) {
                m_buf = ( signals[cur_line[0]] );
            } else
                continue;
        } else if (cur_size == 2) {
            if (is_number(cur_line[1])) {
                m_buf = ( ~ atoi(cur_line[1].c_str()) );
            } else if (signals.find(cur_line[1]) != signals.end()) {
                m_buf = ( ~ signals[cur_line[1]] );
            } else
                continue;
        } else if (cur_size == 3) {
            unsigned short left, right;

            if (is_number(cur_line[0])) {
                left = atoi(cur_line[0].c_str());
            } else if (signals.find(cur_line[0]) != signals.end()){
                left = signals[cur_line[0]];
            } else {
                continue;
            }

            if (is_number(cur_line[2])) {
                right = atoi(cur_line[2].c_str());
            } else if (signals.find(cur_line[2]) != signals.end()){
                right = signals[cur_line[2]];
            } else {
                continue;
            }

            if (cur_line[1] == "AND")
                m_buf = (left & right);
            else if (cur_line[1] == "OR")
                m_buf = (left | right);
            else if (cur_line[1] == "LSHIFT")
                m_buf = ((left << right) & 0xFFFF);
            else if (cur_line[1] == "RSHIFT")
                m_buf = ((left >> right) & 0xFFFF);
            else
                std::cerr << "Unrecognized operation: " << cur_line[1] << std::endl;
        }

        signals[dest] = m_buf;
    }

    std::cout << signals["a"] << std::endl;

    return 0;
}
