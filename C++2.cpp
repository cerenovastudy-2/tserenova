// Реализация хэщ-таблиц
#include <iostream>
#include <list>
#include <vector>
#include <functional>

template<typename K, typename V>
class HashTable {
private:
    std::vector<std::list<std::pair<K, V>>> table;
    size_t capacity;
    
    size_t hashFunction(const K& key) {
        return std::hash<K>{}(key) % capacity;
    }

public:
    HashTable(size_t cap = 10) : capacity(cap) {
        table.resize(capacity);
    }
    
    void insert(const K& key, const V& value) {
        size_t index = hashFunction(key);
        for (auto& pair : table[index]) {
            if (pair.first == key) {
                pair.second = value;
                return;
            }
        }
        table[index].push_back({key, value});
    }
    
    V get(const K& key) {
        size_t index = hashFunction(key);
        for (const auto& pair : table[index]) {
            if (pair.first == key) {
                return pair.second;
            }
        }
        throw std::runtime_error("Key not found");
    }
    
    void remove(const K& key) {
        size_t index = hashFunction(key);
        for (auto it = table[index].begin(); it != table[index].end(); ++it) {
            if (it->first == key) {
                table[index].erase(it);
                return;
            }
        }
        throw std::runtime_error("Key not found");
    }
};

//Бинарные кучи
#include <vector>
#include <algorithm>

template<typename T>
class MinHeap {
private:
    std::vector<T> heap;
    
    void heapifyUp(int index) {
        while (index > 0 && heap[index] < heap[(index-1)/2]) {
            std::swap(heap[index], heap[(index-1)/2]);
            index = (index-1)/2;
        }
    }
    
    void heapifyDown(int index) {
        int smallest = index;
        int left = 2*index + 1;
        int right = 2*index + 2;
        
        if (left < heap.size() && heap[left] < heap[smallest])
            smallest = left;
        if (right < heap.size() && heap[right] < heap[smallest])
            smallest = right;
        
        if (smallest != index) {
            std::swap(heap[index], heap[smallest]);
            heapifyDown(smallest);
        }
    }

public:
    void insert(T value) {
        heap.push_back(value);
        heapifyUp(heap.size()-1);
    }
    
    T extractMin() {
        T min = heap[0];
        heap[0] = heap.back();
        heap.pop_back();
        heapifyDown(0);
        return min;
    }
};