class DynamicArray {
private:
    int* data;
    int size;
    int capacity = 0;
public:

    DynamicArray(int cap = 0) {
        capacity = cap;           // ✓ set member variable
        size = 0;                 // ✓ initialize size
        data = (cap > 0) ? new int[cap] : nullptr;
    }

    int get(int i) {
        return data[i];
    }

    void set(int i, int n) {
        data[i] = n;
    }

    void pushback(int n) {
        if(size >= capacity)
        {
            capacity = (capacity == 0) ? 1 : capacity * 2;  // handle capacity = 0
            int *oldData = data;
            data = new int[capacity];
            for(int i = 0; i < size ; i++)
            {
                data[i] = oldData[i];
            }
            delete[] oldData;              // ✓ free old memory!
        }
        data[size] = n;       // add new element
        size += 1;            // then increment size
    }

    int popback() {
        return data[--size];
    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return capacity;
    }
};
