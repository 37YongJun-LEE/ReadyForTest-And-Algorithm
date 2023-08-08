package com.ssafy.algo;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_17070 {
    // 0809:09:15 시작 (1시간)
	// 종료 0808:10:22 종료 (1시간)
	// 총 (2시간)

	// 필요 요소
    static int N;		// 입력 N
    static int answer;		//정답 출력 위한 answer
    static int[][] arr; 	// 배열저장 arr

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());    // 전역변수 N 입력
        StringTokenizer st;

        // 2차원 배열 입력
        arr = new int[N+1][N+1];
        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
//        System.out.println(Arrays.deepToString(arr)); // 2차원 배열 입력 확인 코드
        
        // 시작지점 가로기준 파이프의 왼쪽좌표(1,1)를 temp,
        // 시작지점 가로기준 파이프의 오른쪽좌표(1,2)를 now라 정하자.
        
        // 파이프  now 부분의 좌표
        int r=1;	// 행
        int c=2; 	// 열

        dfs(0, r, c);
        System.out.println(answer);
        
    }


    // temp 와 now 재설정 필요
    static void dfs(int state, int r, int c) { // now의 r과 c
    	// 대각선으로 진행하는 경우에는 진행방향 앞에있는 3개의 좌표가 모두 0 인 칸이여야한다.	 해당부분처리가 안되어있음
    	
        if (r > N || c > N || arr[r][c] == 1) {  // 기저조건 : 범위를 벗어나거나 , 배열에 1을 만나는 경우 종료
            return;
        } else if (r == N && c == N) {     // N에 도착하면 완료
        	if (state == 1) {
        		if (arr[r][c-1] == 1 || arr[r-1][c] == 1 ) return;	// 대각선 경우만 또 처리하기
        	}
            answer += 1;	// 답 경우 증가
            return;
        }

        // 각 상태에 따라서 진행방향이 결정된다.
        if (state == 0) {   // 가로 : 2개
            dfs(0, r, c+1);
            dfs(1, r+1, c+1);
        } else if (state == 1) {    // 대각선 : 3개
        	
        	if (arr[r][c-1] == 1 || arr[r-1][c] == 1 ) return; 	/// 대각선 처리 부분인데 이부분도 위에 추가 필요하다.
            dfs(0, r, c+1);
            dfs(1, r+1, c+1);
            dfs(2, r+1, c);

        } else { // 세로  : 1개
            dfs(1, r+1, c+1);
            dfs(2, r+1, c);

        }

    }
}
