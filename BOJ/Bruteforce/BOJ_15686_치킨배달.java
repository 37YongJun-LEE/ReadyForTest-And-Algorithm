package boj;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class BOJ_15686_치킨배달 {
	static int N ;
	static int M ;	// 뽑혀야하는 치킨집 개수
	static int[][] map;
	static int answerChickDist; 	// 최종 도시치킨거리
	
	static ArrayList<int[]> houses;  // 모든 집 좌표정보가 담긴 배열
	static ArrayList<int[]> chickens;  // 모든 치킨집 좌표정보가 담긴 배열
	
	static int[][] picked;  // M개 뽑힌 치킨집 좌표정보가 담길 배열
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		N = sc.nextInt();
		M = sc.nextInt();
		houses = new ArrayList<>();
		chickens = new ArrayList<> ();
		
		// 입력과 동시에 집 좌표 배열, 치킨집 좌표 배열 이 필요
		map = new int[N][N];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				map[i][j] = sc.nextInt();
				if (map[i][j] == 1) {
					houses.add(new int[] {i,j});
				} else if (map[i][j] == 2) {
					chickens.add(new int[] {i, j});
				}
			}
		}
		
		picked = new int[M][2];	// M개 뽑힌 치킨집의 좌표 정보 배열
		answerChickDist = Integer.MAX_VALUE;
		
		
		// 치킨집 개수 : chicken.size() 중에서 M개 추출하는 것
		makeCombiAndCalDist(0, 0);
		
		System.out.println(answerChickDist);
		
	}

	

	// 조합 재귀적 구현
	private static void makeCombiAndCalDist(int start, int cnt) {
		if (cnt == M) {
//			System.out.println(Arrays.deepToString(picked));
			// 해당 경우에서 최소 치킨 거리 계산하고 도시 치킨거리 구하기.
			int cityChickDist = 0;
			for(int[] house : houses) {// 현재 집에서 뽑힌 집까지의 거리를 모두 계산하고 최소를 알아내기
				int nowChickDist; // 현재 치킨거리
				int temp = Integer.MAX_VALUE; // 이전 최소 치킨거리 
				for (int[] pick : picked) {
					nowChickDist = Math.abs(house[0] - pick[0]) + Math.abs(house[1] - pick[1]); // 치킨거리계산  
					temp = Math.min(nowChickDist, temp);	// 치킨거리 최소 갱신
				}
//				System.out.println(temp);
				cityChickDist += temp;	// 해당 집의 치킨거리 추가
			}
			// 도시 거리 최소인지 비교;
//			System.out.println(cityChickDist);
			answerChickDist = Math.min(cityChickDist, answerChickDist);
			return;
		}
		
		for (int i = start; i < chickens.size(); i++ ) {
			picked[cnt] = chickens.get(i);
			makeCombiAndCalDist(i + 1 , cnt + 1);	// 조합 적용 i+1이 핵심
		}
		
		
	}
	
}
