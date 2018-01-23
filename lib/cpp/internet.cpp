/*#include<iostream>
#include<fstream>
#include<stdlib.h>*/
#include<bits/stdc++.h>

using namespace std;

class Fuck{
    public: // remove them from public
        int phoneCheck();
        int internetCheck();
};

void Check(){
    string phone = "lsusb | grep -c '2717:ff48'";
    string internet = "/sbin/route -n | grep -c '^0\\.0\\.0\\.0'";
}
int Fuck::phoneCheck(){
    FILE *out = popen("lsusb | grep -c '2717:ff48'","r");// grep Android for general case
    if(!out){
        return 1000;
    }
    unsigned int i;
    fscanf(out,"%u",&i);
    if(i == 1)
        return 0;
    else if(i == 0)
        return 1;
    pclose(out);
    return 0;
}
int Fuck::internetCheck(){

            FILE *output=popen("/sbin/route -n | grep -c '^0\\.0\\.0\\.0'","r");

            if(!output)
            {
                return 1000;
            }
            unsigned int i;
            fscanf(output,"%u",&i);
            if(i == 1)
                return 0;
            else if(i == 0)
                return 1;
            pclose(output);
            return 0;
        }
int main(int argc,char **argv){
FILE *output=popen("/sbin/route -n | grep -c '^0\\.0\\.0\\.0'","r");

if(!output)
{
    return 1;
}
unsigned int i;
fscanf(output,"%u",&i);
if(i == 1)
       return 0;
else if(i == 0)
       return 1;
pclose(output);
return 5;
}

extern "C"
{
    int Fuck_internetCheck(Fuck *fuck) {return fuck->internetCheck();}
    int Fuck_phoneCheck(Fuck *fuck) {return fuck->phoneCheck();}
}
