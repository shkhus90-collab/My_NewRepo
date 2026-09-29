
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JOptionPane;
import javax.swing.JFrame;
import java.awt.event.ActionEvent;

public class NPTEL{
    public static void main(String[] args){
        JFrame frame=new JFrame("NPTEL Java Course");
        JButton button=new JButton("Click Me");
        button.setBounds(50, 100, 100, 40);
        button.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
            JOptionPane.showMessageDialog(null, "Welcome in this Java Course");  
            }
        });
        frame.add(button);
        frame.setSize(300, 200);
        frame.setLayout(null);
        frame.setVisible(true);
    }
}