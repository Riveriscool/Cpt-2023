public class student extends person {
    private int SID;
    private String schoolname; //I forgot what the variables were supposed to be and i couldnt find them so i made these up
    private boolean failing;

    public student(int SID, String schoolname, boolean failing) {
        super();
        this.SID = SID;
        this.schoolname = schoolname;
        this.failing = failing;

    }

    public void set_schoolname(String schoolname) {
        this.schoolname = schoolname;
    }

    public String get_schoolname(){
        return this.schoolname;
    }

    public void set_SID(int SID) {
        this.SID = SID;
    }
    
    public boolean get_failing(){
        return this.failing;
    }

    public void set_failing(boolean failing) {
        this.failing = failing; 
    }

    public String toString() {
        return this.SID + this.schoolname + this.failing + super();
    }
}
