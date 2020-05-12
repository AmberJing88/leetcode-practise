{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "leetcode 247: strobogrammatic number (rotate 180degree same 8,69,1,0)\n",
    "Recurtion Solution complexicity:\n",
    "Time: O(4^n) \n",
    "Space:O(n)\"\"\"\n",
    "\n",
    "def findStrobo(n):\n",
    "    \n",
    "    return find(n, n)\n",
    "\n",
    "def find(m, n):\n",
    "    if m == 0: \n",
    "        return [\"\"]\n",
    "    if m== 1:\n",
    "        return [\"0\", \"1\", \"8\"]\n",
    "    \n",
    "    result = []\n",
    "    center = find(m-2, n)\n",
    "    for c in center:\n",
    "        if m != n:\n",
    "            result.append(\"0\" +c+\"0\")\n",
    "        result.append(\"1\"+c+\"1\")\n",
    "        result.append(\"6\"+c+\"9\")\n",
    "        result.append(\"8\"+c+\"8\")\n",
    "        result.append(\"9\"+c+\"6\")\n",
    "        \n",
    "    return result\n",
    "            \n",
    "            \n",
    "\n",
    "\n",
    "\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['1001',\n",
       " '6009',\n",
       " '8008',\n",
       " '9006',\n",
       " '1111',\n",
       " '6119',\n",
       " '8118',\n",
       " '9116',\n",
       " '1691',\n",
       " '6699',\n",
       " '8698',\n",
       " '9696',\n",
       " '1881',\n",
       " '6889',\n",
       " '8888',\n",
       " '9886',\n",
       " '1961',\n",
       " '6969',\n",
       " '8968',\n",
       " '9966']"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "findStrobo(4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "iteration solution\n",
    "Time: O(5^(n/2))\n",
    "Space: O(5^(n/2))\n",
    "\"\"\"\n",
    "\n",
    "def findStrobo1(n):\n",
    "    \n",
    "    if n <= 0:\n",
    "        return [\"\"]\n",
    "    \n",
    "    if n % 2 ==1:\n",
    "        result = [\"0\", \"1\", \"8\"]\n",
    "    else:\n",
    "        result = [\"\"]\n",
    "    strobo = {\"0\":\"0\", \"1\":\"1\", \"8\":\"8\", \"6\":\"9\", \"9\":\"6\"}\n",
    "    \n",
    "    for i in range(n//2):\n",
    "            \n",
    "        result = [h+res+strobo[h] for h in strobo for res in result]\n",
    "        \n",
    "    return [res for res in result if (res[0] != \"0\" or n ==1)]\n",
    "           "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['1001',\n",
       " '1111',\n",
       " '1881',\n",
       " '1691',\n",
       " '1961',\n",
       " '8008',\n",
       " '8118',\n",
       " '8888',\n",
       " '8698',\n",
       " '8968',\n",
       " '6009',\n",
       " '6119',\n",
       " '6889',\n",
       " '6699',\n",
       " '6969',\n",
       " '9006',\n",
       " '9116',\n",
       " '9886',\n",
       " '9696',\n",
       " '9966']"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "findStrobo1(4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
