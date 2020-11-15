import java.awt.BorderLayout;
import java.awt.FlowLayout;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import java.awt.GridLayout;
import java.awt.GridBagLayout;
import javax.swing.BoxLayout;
import java.awt.Choice;
import java.awt.TextField;
import java.awt.List;
import java.awt.PopupMenu;

import javax.swing.JSpinner;
import javax.swing.JList;
import javax.swing.JMenu;
import javax.swing.JMenuItem;
import java.awt.event.ItemListener;
import java.awt.event.ItemEvent;
import java.awt.Checkbox;
import javax.swing.JCheckBoxMenuItem;

import java.util.*;
import javax.swing.JTextField;

public class testGUI extends JDialog {
	

	private final JPanel contentPanel = new JPanel();
	private JTextField textField;
	private JTextField textField_1;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		try {
			testGUI dialog = new testGUI();
			dialog.setDefaultCloseOperation(JDialog.DISPOSE_ON_CLOSE);
			dialog.setVisible(true);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	/**
	 * Create the dialog.
	 */
	public testGUI() {
		
		setBounds(100, 100, 987, 475);
		getContentPane().setLayout(new BorderLayout());
		contentPanel.setBorder(new EmptyBorder(5, 5, 5, 5));
		getContentPane().add(contentPanel, BorderLayout.CENTER);
		contentPanel.setLayout(null);
		
		JLabel lblNewLabel = new JLabel("View:");
		lblNewLabel.setBounds(96, 127, 61, 24);
		contentPanel.add(lblNewLabel);
		
		String starQuery = "NONE";

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//Begin criteria selectors
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
		Choice choice_reviewCount = new Choice();
		choice_reviewCount.addItemListener(new ItemListener() {
			public void itemStateChanged(ItemEvent e) {
				String review_selection = choice_reviewCount.getSelectedItem();
				switch(review_selection) {
					case "0 - 500":
						System.out.println("0 - 500");
						String starQuery = "1";
						break;
					case "500 - 1000":
						System.out.println("500 - 1000");
						break;
					case "1000 - 1500":
						System.out.println("review_count 1000 - 1500");
						break;
					case "1500 - 2000":
						System.out.println("review_count 1500 - 2000");
						break;
					case "2000+":
						System.out.println("review_count > 2000");
						break;
					default:
						System.out.println("NO SELECTION");
				}
			}
		});
		//PopupMenu popupmenu = new 
		String range1 = new String("0 - 500");
		String range2 = new String("500 - 1000");
		String range3 = new String("1000 - 1500");
		String range4 = new String("1500 - 2000");
		String range5 = new String("2000+");
		choice_reviewCount.add(range1);
		choice_reviewCount.add(range2);
		choice_reviewCount.add(range3);
		choice_reviewCount.add(range4);
		choice_reviewCount.add(range5);
		
		choice_reviewCount.setBounds(302, 217, 75, 22);
		contentPanel.add(choice_reviewCount);
		
/////////////////////////////////////////////////////////////////
		Choice choiceStar = new Choice();
		choiceStar.addItemListener(new ItemListener() {
			public void itemStateChanged(ItemEvent e) {
				String star_selection = choiceStar.getSelectedItem();
				switch(star_selection) {
					case "1 Star":
						System.out.println("stars > 1");
						String starQuery = "1";
						break;
					case "2 Stars":
						System.out.println("stars > 2");
						break;
					case "3 Stars":
						System.out.println("stars > 3");
						break;
					case "4 Stars":
						System.out.println("stars > 4");
						break;
					case "5 Stars":
						System.out.println("stars > 5");
						break;
					default:
						System.out.println("NO SELECTION");
				}
			}
		});
		//PopupMenu popupmenu = new 
		String star1 = new String("1 Star");
		String star2 = new String("2 Stars");
		String star3 = new String("3 Stars");
		String star4 = new String("4 Stars");
		String star5 = new String("5 Stars");
		choiceStar.add(star1);
		choiceStar.add(star2);
		choiceStar.add(star3);
		choiceStar.add(star4);
		choiceStar.add(star5);
		
		choiceStar.setBounds(179, 217, 61, 22);
		contentPanel.add(choiceStar);

		/////////////////////////////////////////////////////////////////

		SortedMap<String, String> states = new TreeMap<String, String>();
		states.put("WY", "test");
		states.put("WI", "test2");
		states.put("WV", "test3");
		states.put("WA", "test");
		states.put("VA", "test2");
		states.put("VT", "test3");
		states.put("UT", "test");
		states.put("TX", "test2");
		states.put("TN", "test3");
		states.put("SD", "test");
		states.put("SC", "test2");
		states.put("RI", "test3");
		states.put("PA", "test");
		states.put("OR", "test2");
		states.put("OK", "test3");
		states.put("OH", "test");
		states.put("ND", "test2");
		states.put("NY", "test3");
		states.put("NM", "test");
		states.put("NJ", "test2");
		states.put("NH", "test3");
		states.put("NV", "test");
		states.put("NE", "test2");
		states.put("MT", "test3");
		states.put("MO", "test");
		states.put("MS", "test2");
		states.put("MN", "test3");
		states.put("MI", "test");
		states.put("MA", "test2");
		states.put("MD", "test3");
		states.put("ME", "test");
		states.put("LA", "test2");
		states.put("KY", "test3");
		states.put("KS", "test");
		states.put("IA", "test2");
		states.put("IN", "test3");
		states.put("IL", "test");
		states.put("ID", "test2");
		states.put("HI", "test3");
		states.put("GA", "test");
		states.put("FL", "test2");
		states.put("DE", "test3");
		states.put("CT", "test");
		states.put("CO", "test2");
		states.put("CA", "test3");
		states.put("AR", "test");
		states.put("AZ", "test2");
		states.put("AK", "test3");
		states.put("AL", "test");

		Choice choiceState = new Choice();
		choiceState.addItemListener(new ItemListener() {
			public void itemStateChanged(ItemEvent e) {
				String state_selection = choiceState.getSelectedItem();
				try {
					System.out.println(states.get(state_selection));
				}catch(Exception ex){
					System.out.println("no selection");
				}
			}
		});
		// PopupMenu popupmenu = new 

		Set<String> keys = states.keySet();

		for(String key : keys){
			choiceState.add(key);
		}

		choiceState.setBounds(589, 217, 61, 22);
		contentPanel.add(choiceState);
	
		////////////////////////////////////////////////////////////
		
		
		
		
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//END criteria selectors
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
		{
			Checkbox checkbox = new Checkbox("review count");
			checkbox.setBounds(618, 127, 97, 24);
			contentPanel.add(checkbox);
		}
		{
			Checkbox checkbox = new Checkbox("stars");
			checkbox.setBounds(556, 127, 56, 24);
			contentPanel.add(checkbox);
		}
		{
			Checkbox checkbox = new Checkbox("state");
			checkbox.setBounds(397, 127, 56, 24);
			contentPanel.add(checkbox);
		}
		{
			Checkbox checkbox = new Checkbox("city");
			checkbox.setBounds(345, 127, 46, 24);
			contentPanel.add(checkbox);
		}
		{
			Checkbox checkbox = new Checkbox("address");
			checkbox.setBounds(266, 127, 73, 24);
			contentPanel.add(checkbox);
		}
		{
			Checkbox checkbox = new Checkbox("postal code");
			checkbox.setBounds(459, 127, 91, 24);
			contentPanel.add(checkbox);
		}
		{
			Checkbox checkbox = new Checkbox("business");
			checkbox.setBounds(179, 127, 81, 24);
			contentPanel.add(checkbox);
		}
		{
			JLabel lblNewLabel_1 = new JLabel("Search Criteria:");
			lblNewLabel_1.setBounds(58, 183, 99, 16);
			contentPanel.add(lblNewLabel_1);
		}
		{
			JLabel lblNewLabel_2 = new JLabel("Stars");
			lblNewLabel_2.setBounds(184, 183, 56, 16);
			contentPanel.add(lblNewLabel_2);
		}
		{
			JLabel lblNewLabel_3 = new JLabel("Review_Count");
			lblNewLabel_3.setBounds(302, 183, 97, 16);
			contentPanel.add(lblNewLabel_3);
		}

		{
			JLabel lblNewLabel_4 = new JLabel("State");
			lblNewLabel_4.setBounds(589, 183, 97, 16);
			contentPanel.add(lblNewLabel_4);
		}
		
		JLabel lblNewLabel_5 = new JLabel("City");
		lblNewLabel_5.setBounds(426, 178, 92, 26);
		contentPanel.add(lblNewLabel_5);
		
		JLabel lblNewLabel_6 = new JLabel("Postal Code");
		lblNewLabel_6.setBounds(680, 178, 92, 26);
		contentPanel.add(lblNewLabel_6);
		
		textField = new JTextField();
		textField.setBounds(388, 217, 186, 32);
		contentPanel.add(textField);
		textField.setColumns(10);
		
		textField_1 = new JTextField();
		textField_1.setBounds(680, 217, 186, 32);
		contentPanel.add(textField_1);
		textField_1.setColumns(10);
		
		
		{
			PopupMenu popup = new PopupMenu("test");
			
		}
		{
			JPanel buttonPane = new JPanel();
			buttonPane.setLayout(new FlowLayout(FlowLayout.RIGHT));
			getContentPane().add(buttonPane, BorderLayout.SOUTH);
			{
				JButton okButton = new JButton("OK");
				okButton.setActionCommand("OK");
				buttonPane.add(okButton);
				getRootPane().setDefaultButton(okButton);
			}
			{
				JButton cancelButton = new JButton("Cancel");
				cancelButton.setActionCommand("Cancel");
				buttonPane.add(cancelButton);
			}
		}
	}
}
