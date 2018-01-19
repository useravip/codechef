#include<iostream>
 
using namespace std;
 
int main(){
int n;
cin>>n;
int max = 0 , smax =0;
for(int w=n; w!=0; w--){
    int *arr = new int[3];
    for(int i = 0; i<3; i++){
        cin>>arr[i];
    }
 
for (int j=0; j<3; j++){
    if(arr[j] > max){
        smax = max;
        max = arr[j];
    }
    else{
    if(arr[j]>smax){
        smax = arr[j];
    }
    }
}
cout<<smax<<endl;
max = 0, smax =0;
}
 
return 0;
}
 
