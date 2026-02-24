public class LLNode {
    int data;
    LLNode next;

    public LLNode(int data) {
        this.data = data;
        this.next = null;
    }
}

public class Queue {
    private LLNode head;
    private LLNode tail;

    public Queue() {
        this.head = null;
        this.tail = null;
    }

    public int front() {
        if (head == null) {
            throw new IllegalStateException("Queue is empty");
        }
        return head.data;
    }

    public int back() {
        if (tail == null) {
            throw new IllegalStateException("Queue is empty");
        }
        return tail.data;
    }

    public void enqueue(int data) {
        LLNode newNode = new LLNode(data);
        if (tail == null) {
            head = tail = newNode;
        } else {
            tail.next = newNode;
            tail = newNode;
        }
    }

    public int dequeue() {
        if (head == null) {
            throw new IllegalStateException("Queue is empty");
        }
        int dequeuedData = head.data;
        head = head.next;
        if (head == null) {
            tail = null;
        }
        return dequeuedData;
    }
}