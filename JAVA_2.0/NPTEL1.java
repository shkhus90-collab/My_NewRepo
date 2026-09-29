import javax.swing.*;
public class NPTEL1 {
    public class NPTEL1 extends JFrame{
        JButton button;
        public NPTEL1(){
            button=new JButton("Programmung in Java");
            add(button);
            setSize(300,200);
            setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            setVisible(true);
        }
        public static void main(String[] args) {
            new NPTEL1();
        }}
    }
    
}
