public class grad extends student {
    private String research;

    public grad (String research) {
        super(SID, schoolname, failing);
        this.research = research;

    }
    public static int getVacationDays() {
        return 0;// no vacation for you :(

    }
    public void set_research(String newresearch){
        this.research = newresearch;
    }
    public String get_Research() {
        return this.research;
    }
}