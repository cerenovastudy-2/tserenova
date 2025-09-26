//Реализация хэш-таблиц
import java.util.LinkedList;

public class HashTable<K, V> {
    private class Pair {
        K key;
        V value;
        
        Pair(K key, V value) {
            this.key = key;
            this.value = value;
        }
    }
    
    private LinkedList<Pair>[] table;
    private int capacity;
    
    @SuppressWarnings("unchecked")
    public HashTable(int capacity) {
        this.capacity = capacity;
        table = new LinkedList[capacity];
        for (int i = 0; i < capacity; i++) {
            table[i] = new LinkedList<>();
        }
    }
    
    private int hashFunction(K key) {
        return Math.abs(key.hashCode()) % capacity;
    }
    
    public void put(K key, V value) {
        int index = hashFunction(key);
        for (Pair pair : table[index]) {
            if (pair.key.equals(key)) {
                pair.value = value;
                return;
            }
        }
        table[index].add(new Pair(key, value));
    }
    
    public V get(K key) {
        int index = hashFunction(key);
        for (Pair pair : table[index]) {
            if (pair.key.equals(key)) {
                return pair.value;
            }
        }
        throw new RuntimeException("Key not found");
    }
    
    public void remove(K key) {
        int index = hashFunction(key);
        for (Pair pair : table[index]) {
            if (pair.key.equals(key)) {
                table[index].remove(pair);
                return;
            }
        }
        throw new RuntimeException("Key not found");
    }
}


