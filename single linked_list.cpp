#include <iostream>
using namespace std;

class Node {
public:
    string name;
    long prn;
    Node* next;

Node(string n, long p){
    name=n;
    prn=p;
    next=nullptr;
}
};

class MemberList {
private:
    Node* head;
    Node* tail;

public:
    MemberList(){
        head=nullptr;
        tail=nullptr;
    }

    void addPresident() {
        string name;
        long prn;
        cout << "Enter the name of the president: ";
        cin >> name;
        cout << "Enter the PRN number: ";
        cin >> prn;

        Node* temp = new Node(name, prn);
        temp->next = head;
        head = temp;

        if (tail == nullptr) {
            tail = head;  // Set tail if list was empty
        }
    }

    void addSecretary() {
        string name;
        long prn;
        cout << "Enter the name of the secretary: ";
        cin >> name;
        cout << "Enter the PRN number: ";
        cin >> prn;

        Node* temp = new Node(name, prn);
        if (tail) {
            tail->next = temp;
        } else {
            head = temp;  // If list was empty
        }
        tail = temp;  // Update tail
    }

    void addMember() {
        string name;
        long prn;
        cout << "Enter the name of the member: ";
        cin >> name;
        cout << "Enter the PRN number: ";
        cin >> prn;

        Node* temp = new Node(name, prn);
        if (head) {
            temp->next = head->next;
            head->next = temp;
        } else {
            head = temp;  // If list was empty
            tail = temp;  // Update tail if it's the first member
        }
    }

    void deleteMember() {
        long prn;
        cout << "Enter the PRN number to delete: ";
        cin >> prn;

        if (head == nullptr) return;  // List is empty

        if (head->prn == prn) {
            Node* toDelete = head;
            head = head->next;
            delete toDelete;
            if (head == nullptr) tail = nullptr;  // List is now empty
            return;
        }

        Node* temp = head;
        while (temp->next && temp->next->prn != prn) {
            temp = temp->next;
        }

        if (temp->next) {
            Node* toDelete = temp->next;
            temp->next = temp->next->next;
            if (temp->next == nullptr) tail = temp;  // Update tail if needed
            delete toDelete;
        } else {
            cout << "Member not found!" << endl;
        }
    }

    int totalNumberOfMembers() {
        Node* temp = head;
        int count = 0;
        while (temp) {
            count++;
            temp = temp->next;
        }
        return count;
    }

    void displayMembers() {
        Node* temp = head;
        cout << "Members List:" << endl;
        while (temp) {
            cout << "Name: " << temp->name << ", PRN: " << temp->prn << endl;
            temp = temp->next;
        }
    }

    ~MemberList() {
        while (head) {
            Node* temp = head;
            head = head->next;
            delete temp;
        }
    }
};

int main() {
    MemberList list;
    int choice;

    do {
        cout << "\nMenu:\n";
        cout << "1. Add President\n";
        cout << "2. Add Secretary\n";
        cout << "3. Add Member\n";
        cout << "4. Delete Member\n";
        cout << "5. Total Number of Members\n";
        cout << "6. Display Members\n";
        cout << "7. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                list.addPresident();
                break;
            case 2:
                list.addSecretary();
                break;
            case 3:
                list.addMember();
                break;
            case 4:
                list.deleteMember();
                break;
            case 5:
                cout << "Total Members: " << list.totalNumberOfMembers() << endl;
                break;
            case 6:
                list.displayMembers();
                break;
            case 7:
                cout << "Exiting..." << endl;
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    } while (choice != 7);

    return 0;
}
