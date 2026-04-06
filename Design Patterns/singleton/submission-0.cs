public class Singleton {
    private string value = null;
    private static Singleton cur = null;

    private Singleton() {
      
    }

    public static Singleton getInstance() {
        if(cur == null)
        {
            cur = new();
        }
        return cur;
    }

    public string getValue() {
        return this.value;
    }

    public void setValue(string value){
        this.value = value;
    }
}
