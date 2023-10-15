package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_7569_토마토 {
	static int M, N, H;
	static int[][][] Box;		/// 방문리스트이자 토마토 상태 리스트
	static int answer;
	
	static ArrayList<int[]> tomatoList;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		M = Integer.parseInt(st.nextToken());
		N = Integer.parseInt(st.nextToken());
		H = Integer.parseInt(st.nextToken());
		
		Box = new int[H][N][M];	// H층, N행 ,M열
		tomatoList = new ArrayList<>();
		for (int h = 0; h < H; h++) {
			for (int r = 0; r < N; r++) {
				st = new StringTokenizer(br.readLine());
				for (int c = 0; c < M; c++) {
					Box[h][r][c] = Integer.parseInt(st.nextToken());		// h층에 있는  (r,c)위치 토마토 상태
					if (Box[h][r][c] == 1) tomatoList.add(new int[] {h, r, c, 0});
				}
			}
		}
//		System.out.println(Arrays.deepToString(Box));
		
		// 1은 익은 토마토, 0은 안익은 토마토, -1은 토마토가 없는칸
		
		// 관통 조건 : 하루에, 상태가 1인 토마토(익은토마토) 기준으로 6방향으로 인접한 토마토가 익는다. 
		
		// bfs로 풀이한다. 
		
		// 큐에 시작하는 첫날 익은 토마토를 먼저 큐에 넣는다. 큐에 들어가는 정보는 익은 토마토의 좌표 h,r,c 와 시작 날짜인 숫자를 적는다 (시작 = 0)
		// 큐가 전부 빌때까지 반복한다. 
		// 큐를 나올때마다 최대 날짜를 갱신한다. 
		answer = 0;
		bfs();
		// 마지막에 상태를 체크하는 부분 필요 -> -1때문에 익기 진행 못할 수 도 있기때문이다.
		if (!check()) answer = -1;
		System.out.println(answer);		// answer가 한번도 갱신이 되지 않는다면 0으로 출력: 모두 익은 1이라면 아무런 진행도 하지 않기때문,
		
		
	}
	private static boolean check() {
		for (int h = 0; h < H; h++) {
			for (int r = 0; r < N; r++) {
				for (int c = 0; c < M; c++) {
					if (Box[h][r][c] == 0) return false;
				}
			}
		}
		return true;
	}
	static int[] dh = {-1, 1, 0, 0, 0, 0};
	static int[] dr = {0, 0, -1, 1, 0, 0};
	static int[] dc = {0, 0, 0, 0, -1, 1};
	
	private static void bfs() {
		Queue<int[]> queue = new ArrayDeque<>();
		for (int i = 0 ; i < tomatoList.size(); i++) {
			queue.offer(tomatoList.get(i));
			// 방문체크 원래 해야하지만 상태 1 자체가 방문상태이므로 , 여기선 생략
		}
		
		while(!queue.isEmpty()) {
			int[] v = queue.poll();
			
			int h = v[0];
			int r = v[1];
			int c = v[2];
			int day = v[3];
			
			if (answer < day) answer = day;
			
			for (int d = 0; d < 6; d++) {
				int nh = h + dh[d];
				int nr = r + dr[d];
				int nc = c + dc[d];
				// day는 기달
				if (nh < 0 || nr < 0 || nc < 0 || nh >= H || nr >= N || nc >= M || Box[nh][nr][nc] == -1 || Box[nh][nr][nc] == 1) continue;
				queue.offer(new int[] {nh, nr, nc, day + 1}); // 하루 지나서,
				Box[nh][nr][nc] = 1;						  // 익은상태,,
			}
		}
		
		
	}

}
