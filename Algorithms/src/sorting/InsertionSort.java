/**
 * Algorithm 1 - Insertion Sort [Random generated 10 numbers] - Ascending and Descending
 */
package sorting;
import java.util.Random;

/**
 * @author arun pottekat
 *
 */
public class InsertionSort {

	int new_array[] = new int[10];

	public InsertionSort(){
		Random rand = new Random();
		for (int i=9; i>=0; i--) {
			new_array[9-i] = rand.nextInt(100);
		}
	}

	public int display(){
		for (int i=0; i<10; i++) {
			System.out.println(new_array[i]);
		}
		return 0;
	}
	
	public int sortModule(String type){
		if(type == "ASCENDING") {
			for(int j=1; j<10; j++) {
				int key = new_array[j];
				int i = j - 1;
				while(i >= 0 && key < new_array[i]) {
					new_array[i+1] = new_array[i];
					i = i - 1;
				}
				new_array[i+1] = key;
			}
		}
		else {
			for(int j=1; j<10; j++) {
				int key = new_array[j];
				int i = j - 1;
				while(i >= 0 && key > new_array[i]) {
					new_array[i+1] = new_array[i];
					i = i - 1;
				}
				new_array[i+1] = key;
			}	
		}
		return 0;
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		InsertionSort insert = new InsertionSort();
		System.out.println("Initial Sequence");
		insert.display();
		System.out.println("Sorted Sequence");
		String type[] = {"ASCENDING", "DESCENDING"};
		for(int i=0; i<2; i++) {
			System.out.println(type[i] + " SORT");
			insert.sortModule(type[i]);
			insert.display();
		}
	}
}
