public class DynamicArray {

    private int capacity = 3;
    private int size = 0;
    private int[] dynamicArray;

    public DynamicArray(int capacity) {
        if(capacity > 0)
        {
            this.capacity = capacity;
        }
        this.dynamicArray = new int[capacity];
    }

    public int Get(int i) {
        return this.dynamicArray[i];
    }

    public void Set(int i, int n) {
        this.dynamicArray[i] = n;
    }

    public void PushBack(int n) {
        if(size == capacity)
        {
            Resize();
        }
        this.dynamicArray[size] = n;
        this.size += 1;
    }

    public int PopBack() {
        return this.dynamicArray[--size];
    }

    private void Resize() {
        int[] a = new int[this.capacity*2];
        for(int i = 0 ; i < size ; i++)
        {
            a[i] = this.dynamicArray[i];
        }
        this.capacity *= 2;
        this.dynamicArray = a;
    }

    public int GetSize() {
        return size;
    }

    public int GetCapacity() {
        return this.capacity;
    }
}