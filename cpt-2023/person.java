public class person {
    private int SSN;
    private String name;
    private boolean alive;
    private int age;

    public person() {

    }
    public person(int SSN, String name, boolean alive, int age) {
        this.SSN = SSN;
        this.name = name;
        this.alive = alive;
        this.age = age;
    }


    public void set_SSN(int SSN) {
        this.SSN = SSN;
    }
    
    public int get_SSN() {
        return this.SSN;
    }
    public void set_name(String name){
        this.name = name;
    }
    public String get_name(){
        return this.name;
    }
    public void set_alive(boolean alive) {
        this.alive = alive;
    }
    public boolean get_alive() {
        return this.alive;
    }
    public void set_age(int age) {
        this.age = age;
    }
    public int get_age() {
        return this.age;
    }
    public String toString(){
        return this.age + this.SSN + this.alive + this.name;
    }

    

}