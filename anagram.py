{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a87f5ebb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I\n",
      "IN\n",
      "IND\n",
      "INDI\n",
      "INDIA\n"
     ]
    }
   ],
   "source": [
    "str=\"INDIA\"\n",
    "x=\"\"\n",
    "for i in str:\n",
    "    x+=i\n",
    "    print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "39f1c889",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The strings aren't anagrams.\n"
     ]
    }
   ],
   "source": [
    "# function to check if two strings are\n",
    "# anagram or not\n",
    "def check(s1, s2):\n",
    "\t\n",
    "\t# the sorted strings are checked\n",
    "\tif(sorted(s1)== sorted(s2)):\n",
    "\t\tprint(\"The strings are anagrams.\")\n",
    "\telse:\n",
    "\t\tprint(\"The strings aren't anagrams.\")\t\t\n",
    "\t\t\n",
    "# driver code\n",
    "s1 =\"listen\"\n",
    "s2 =\"hi\"\n",
    "check(s1, s2)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2fe7d600",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "  * *  \n",
      " *  * * \n",
      "*   *  \n",
      " * * *  \n",
      " * * *  \n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "for i in range(n):\n",
    "    for j in range(n):\n",
    "        if i+j==n//2 or i-j==n//2 or j-1==n//2 or i+j==n+1:\n",
    "            print(\"*\",end=\" \")\n",
    "        else:\n",
    "            print(end=\" \")\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1932c01b",
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
