This is my submission for the QOSF Mentorship Programme 2021. I will be tackling Task 2. My approach to the problem and all necessary calculations and steps have been highlighted in the notebook. Please find my solution in the file:  **_Solution.ipynb_**

If the notebook (or any of the MathJax in it) is not rendered correctly on GitHub, please view it on nbviewer instead.

I am sincerely thankful to QOSF, for giving tasks that challenge us and make us push our boundaries. I personally learnt a lot while attempting this task.


Thank you!

Amrita Pandey

<hr> <br>

# Task 2 - QOSF Screening Tasks (cohort3)

The bit-flip code and the sign-flip code are two very simple circuits able to detect and fix the bit-flip and the sign-flip errors, respectively.

1.	Build the simple circuit to prepare the Bell state.

2.	Now add, right before the CNOT gate and for each of the two qubits, an arbitrary “error gate”. By error gate we mean that with a certain probability (that you can decide but   must be non-zero for all the choices) you have a 1 qubit unitary which can be either the identity, or the X gate (bit-flip error) or the Z gate (sign-flip error).

3.	Encode each of the two qubits with a sign-flip or a bit-flip code, in such a way that all the possible choices for the error gates described in 2), occurring on the logical qubits, can be detected and fixed. Motivate your choice. This is the most non-trivial part of the problem, so do it with a lot of care!

4.	Test your solution by making many measurements over the final state and testing that the results are in line with the expectations.

<br>
