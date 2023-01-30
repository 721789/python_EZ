{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "fdbc8099",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter choice from ['rock', 'paper', 'scissor']rock\n",
      "computer choice: paper\n",
      "enter choice from ['rock', 'paper', 'scissor']paper\n",
      "computer choice: rock\n",
      "enter choice from ['rock', 'paper', 'scissor']scissor\n",
      "computer choice: paper\n",
      "enter choice from ['rock', 'paper', 'scissor']rock\n",
      "computer choice: scissor\n",
      "enter choice from ['rock', 'paper', 'scissor']paper\n",
      "computer choice: scissor\n",
      "enter choice from ['rock', 'paper', 'scissor']scissor\n",
      "computer choice: paper\n",
      "enter choice from ['rock', 'paper', 'scissor']rock\n",
      "computer choice: scissor\n",
      "player  wins\n"
     ]
    }
   ],
   "source": [
    "from random import randint\n",
    "choice=['rock','paper','scissor']\n",
    "s1=0\n",
    "s2=0\n",
    "n=0\n",
    "limit=5\n",
    "while(True):\n",
    "    p=input(f\"enter choice from {choice}\").lower()\n",
    "    comp=choice[randint(0,2)]\n",
    "    print(\"computer choice:\",comp)\n",
    "    if p==comp:\n",
    "        s1+=1\n",
    "    elif p=='paper' and comp=='rock':\n",
    "        s1+=1\n",
    "    elif p=='rock' and comp=='scissor':\n",
    "        s1+=1\n",
    "    elif p=='scissor' and comp=='paper':\n",
    "        s1+=1\n",
    "    else:\n",
    "        s2+=1\n",
    "    if s1==limit or s2==limit:\n",
    "         break\n",
    "if s1>s2:\n",
    "    print(\"player  wins\")\n",
    "else:\n",
    "    print(\"system  wins\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "44382808",
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
