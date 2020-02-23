public class BitonicArray {
    public static void main(String args[]){
        int arr[] = {1,2,3,4,5,4,3};
        int n = arr.length;
        int index = searchBitonicPoint(arr, 0, n-1);
        int key = 1;
        int x = searchBitonic(arr, n, index, key);
        if(x != -1){
            System.out.println("Element found!");
        } else{
            System.out.println("Element can not be found!");
        }
    }

    public static int searchBitonic(int arr[], int n, int index, int key){
        if(key > arr[index]){
            return -1;
        } else if(key == arr[index]) {
            return index;
        } else{
            int temp = ascendingBinarySearch(arr, 0, index-1, key);
            if(temp != -1){
                return temp;
            }
            else{
                return descendingBinarySearch(arr, index+1, n - 1, key);
            }
        }
    }

    public static int searchBitonicPoint(int arr[], int l, int r){
        l = 0;
        r = arr.length -1;

        if(arr.length == 1){
            return arr[0];
        }

        int mid = ( (l+r)/2 );

        if(mid > mid +1 && mid > mid - 1){
            return mid;
        }
        else if(mid < mid +1 && mid < mid -1){
            searchBitonicPoint(arr, mid, r);
        } else if(mid < mid -1 && mid > mid +1){
            searchBitonicPoint(arr, l, mid);
        }
        return mid;
    }

    public static int ascendingBinarySearch(int arr[], int low, int high, int key){
        while(low <= high){
            int mid = (low + high)/2 ;
            if(arr[mid] == arr[key]){
                return mid;
            } else if(arr[mid] > arr[key]){
                high = mid - 1;
            } else if(arr[mid] < arr[key]){
                low = mid + 1;
            }
        }
        return -1;
    }

    public static int descendingBinarySearch(int arr[], int low, int high, int key){
        while(low <= high){
            int mid = (low+high)/2 ;
            if(arr[mid] == arr[key]){
                return mid;
            } else if(arr[mid] > arr[key]){
                high = mid - 1;
            } else if(arr[mid] < arr[key]){
                low = mid + 1;
            }
        }
        return -1;
    }


}
