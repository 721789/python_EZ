{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7bae8a33",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Preethi\n",
      "1039\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "class Student:\n",
    "    name=\"Preethi\"\n",
    "    __rn=1039 #prvate var\n",
    "    def get_rollno(self):\n",
    "        return self.__rn\n",
    "    def set_rollno(self,newval):\n",
    "        self.__rn=newval\n",
    "obj=Student()\n",
    "print(obj.name)\n",
    "print(obj.get_rollno())\n",
    "print(obj.set_rollno(39))\n",
    "#private var cannot be accessed even with the class object to access the private var we use getter() and setter() methods"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "17f2d555",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "Enter user name: preethi\n",
      "Enter password: 123\n",
      "Enter user name: pujitha\n",
      "Enter password: 345\n",
      "Enter user name: rimsha\n",
      "Enter password: 567\n",
      "Enter user name: a\n",
      "Enter password: 444\n",
      "Enter user name: b\n",
      "Enter password: 444\n",
      "{'preethi': '123', 'pujitha': '345', 'rimsha': '567', 'a': '444', 'b': '444'}\n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "d = {}\n",
    "\n",
    "for i in range(n):\n",
    "    name = input(\"Enter user name: \")\n",
    "    passward = input(\"Enter password: \")\n",
    "    d[name] = passward\n",
    "print(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "bc85d230",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "Enter user name: p\n",
      "Enter password: r\n",
      "Enter user name: pp\n",
      "Enter password: r\n",
      "[{'p': 'r'}, {'pp': 'r'}]\n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "arr = []\n",
    "\n",
    "for i in range(n):\n",
    "    name = input(\"Enter user name: \")\n",
    "    passward = input(\"Enter password: \")\n",
    "    arr.append({name:passward})\n",
    "\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "ff5c3793",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "Enter user name: u1\n",
      "Enter password: p1\n",
      "Enter user name: u2\n",
      "Enter password: p2\n",
      "[{'u1': 'p1'}, {'u2': 'p2'}]\n",
      "enter a nameu1\n",
      "passwardp1\n",
      "valid passward\n"
     ]
    }
   ],
   "source": [
    "#validation of passward\n",
    "n=int(input())\n",
    "arr = []\n",
    "\n",
    "for i in range(n):\n",
    "    name = input(\"Enter user name: \")\n",
    "    passward = input(\"Enter password: \")\n",
    "    arr.append({name:passward})\n",
    "\n",
    "print(arr)\n",
    "u1=input(\"enter a name\")\n",
    "p1=input(\"passward\")\n",
    "f=False\n",
    "for obj in arr:\n",
    "    try: \n",
    "        passward=obj[u1]\n",
    "        f=True\n",
    "        if p1==passward:\n",
    "             print(\"valid passward\")\n",
    "        else:\n",
    "            print(\"invalid\")\n",
    "    except:\n",
    "        pass\n",
    "if f==False:\n",
    "    print(\"User not found\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ce8bc62c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
