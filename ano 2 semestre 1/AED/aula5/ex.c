#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef long long ll;

ll t1_calls;
ll t2_calls;
ll t3_calls;

ll T1(int n) {
	t1_calls++;
	if (n <= 1) return 1;
	return T1(n/2) + n;
}

ll T2(int n) {
	t2_calls++;
	if (n <= 1) return 1;
	int a = n/2;            // floor(n/2)
	int b = (n+1)/2;        // ceil(n/2)
	return T2(a) + T2(b) + n;
}

ll T3(int n) {
	t3_calls++;
	if (n <= 1) return 1;
	if ((n % 2) == 0) {
		ll half = T3(n/2);
		return 2*half + n;
	} else {
		int a = n/2;      /* floor */
		int b = (n+1)/2;  /* ceil */
		return T3(a) + T3(b) + n;
	}
}

int main(int argc, char **argv) {
	int N = 64; /* default */
	if (argc >= 2) {
		N = atoi(argv[1]);
		if (N < 1) N = 1;
	}

	printf("# n\tT1(n)\tCalls1\tT2(n)\tCalls2\tT3(n)\tCalls3\n");
	for (int n = 1; n <= N; ++n) {
		t1_calls = t2_calls = t3_calls = 0;
		ll v1 = T1(n);
		ll c1 = t1_calls;

		t2_calls = 0;
		ll v2 = T2(n);
		ll c2 = t2_calls;

		t3_calls = 0;
		ll v3 = T3(n);
		ll c3 = t3_calls;

		printf("%d\t%lld\t%lld\t%lld\t%lld\t%lld\t%lld\n", n, v1, c1, v2, c2, v3, c3);
	}

	return 0;
}
