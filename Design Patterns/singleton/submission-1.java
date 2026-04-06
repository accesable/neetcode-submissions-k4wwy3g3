static class Singleton {
    private String value = null; 
    private static Singleton current = null;

    private Singleton() {
    }

    public static Singleton getInstance() {
        if(current == null)
        {
            current = new Singleton();
        }
        return current;
    }

    public String getValue() {
        return this.value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    
}
