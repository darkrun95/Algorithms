/**
 * 
 */
package searching;
import java.util.Random;

/**
 * @author arun
 *
 */
public class LinearSearch {

	/**
	 * @param args
	 */
	int new_array[] = new int[10];

	public LinearSearch(){
		Random rand = new Random();
		for (int i = 9; i >= 0; i--) {
			new_array[9-i] = rand.nextInt(20);
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int keyValue = 19;
		LinearSearch linear = new LinearSearch();
		
		System.out.println("Base Array");
		linear.displayArray();
		boolean returnVal = linear.linearSearch(keyValue);
		if (returnVal) {
			System.out.println("Value Found");
		}
		else {
			System.out.println("Value Not Found");
		}
	}

	private int displayArray() {
		// TODO Auto-generated method stub
		for (int i = 0; i < new_array.length; i++) {
			System.out.print(new_array[i] + " ");
		}
		System.out.println();
		return 0;
	}

	private boolean linearSearch(int keyValue) {
		// TODO Auto-generated method stub
		for (int i = 0; i < new_array.length; i++) {
			if (new_array[i] == keyValue) {
				return true;
			}
		}
		return false;
	}

}
