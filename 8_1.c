#include <stdio.h>
#include <stdlib.h>
 struct btnode
{
    int value;
    struct btnode *l;
    struct btnode *r;
}*root = NULL, *temp = NULL, *t2, *t1;
int flag = 1;
void main()
{
    int ch;
    printf("\nOPERATIONS ---");
    printf("1.create()\n2.display()");
    while(1)
     {
        printf("\nEnter your choice : ");
        scanf("%d",&ch);
        switch(ch)
        {
           case 1:create();break;
           case 2:display();break;
           case 3:exit(0);
          default :printf("Wrong choice, Please enter correct choice  ");break;    
        }
    }
}
 
/* To insert a node in the tree */
void insert()
{
    if (root == NULL) 
        root = temp;
    else    
        search(root);    
}
 
/* To create a node */
void create(struct btnode *t)
{
    int data;
    printf("Enter data of node to be inserted : ");
    scanf("%d", &data);
    temp = (struct btnode *)malloc(1*sizeof(struct btnode));
    temp->value = data;
    temp->l = temp->r = NULL;
    insert();
}
/* Function to search the appropriate position to insert the new node */
void search(struct btnode *t)
{
    if ((temp->value > t->value) && (t->r != NULL))      /* value more than root node value insert at right */
        search(t->r);
    else if ((temp->value > t->value) && (t->r == NULL))
        t->r = temp;
    else if ((temp->value < t->value) && (t->l != NULL))    /* value less than root node value insert at left */
        search(t->l);
    else if ((temp->value < t->value) && (t->l == NULL))
        t->l = temp;
}


void display(struct btnode *t)
{
    if (root == NULL)
    {
        printf("No elements in a tree to display");
        return;
    }
    if (t->r != NULL)    
        display(t->r);
    printf("%d -> ", t->value);
    if (t->l != NULL)    
        display(t->l);
    printf("%d -> ", t->value);
}

