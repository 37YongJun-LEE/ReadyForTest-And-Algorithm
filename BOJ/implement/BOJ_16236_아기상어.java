package boj;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_16236_아기상어 {

	static int N;
	static int[][] Map;
	static ArrayList<Fish> FishList;
	static int answer;
	
	static Shark shark;
	static class Shark {
		int r, c, size, exp;
		public Shark(int r, int c, int size, int exp) {
			super();
			this.r = r;
			this.c = c;
			this.size = size;
			this.exp = exp;
		}
	}
	
	static class Fish {
		int r, c, size, d;
		public Fish(int r, int c, int size, int d) {
			super();
			this.r = r;
			this.c = c;
			this.size = size;
			this.d = d;
		}
		@Override
		public String toString() {
			return "Fish [r=" + r + ", c=" + c + ", size=" + size + ", d=" + d + "]";
		}
	}
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		Map = new int[N][N];
		FishList = new ArrayList<>();
		answer = 0;
		
		StringTokenizer st;
		// 맵 정보 입력 + 물고기 정보 입력, 물고기리스트 넣기
		for (int i = 0 ; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				Map[i][j] = Integer.parseInt(st.nextToken());
				if (Map[i][j] > 0 && Map[i][j] < 9) FishList.add(new Fish(i, j, Map[i][j], Integer.MAX_VALUE));	// 물고기 정보 입력
				else if (Map[i][j] == 9) shark = new Shark(i, j, 2, 0);
			}
		}
		// 최초의 단 한번만 맵의 9 지우기
		Map[shark.r][shark.c] = 0;
		
		// 시뮬레이션은 먹기 가능한 물고기가 전부 없어질 때까지 반복한다.
		int cnt = 0;
		while (!FishList.isEmpty()) {				// FishList.isEmpty()라면 엄마상어 호출과 동일하다.
			// 1. 각 물고기와의 거리구하기.
			for (Fish fish : FishList) {
				fish.d = bfs(fish);	// 상어의 좌표와 fish의 좌표를 아니까 bfs를 돌려서 좌표구하기.
//				System.out.print(fish.d + " ");
			}
			
			// 2. 리스트를 정렬하기 -> 거리순, 가장왼쪽순
			Collections.sort(FishList, (f1, f2) -> {
				if (f1.d - f2.d == 0 && f1.r - f2.r == 0) return f1.c - f2.c; // 거리동일, 같은 높이,-> 가장 왼쪽 정렬
				if (f1.d - f2.d == 0) return f1.r - f2.r;	//거리 동일의 경우,-> 가장 위쪽 정렬
				return f1.d - f2.d;	// 거리 가장 가까운 순 정렬
			});
//			System.out.println(FishList);
			
			// 3. 잡아먹으러 이동하기 + 좌표의 이동시간 계산하기 + 먹고 상어 크기 성장하기.
			// 판단먼저하기 먹기가능한지..
			boolean noEntry = false;
			for (int i = 0; i < FishList.size(); i++) {
				if (FishList.get(i).size < shark.size && FishList.get(i).d != Integer.MAX_VALUE ) {
					shark.r = FishList.get(0).r;
					shark.c = FishList.get(0).c;
//					System.out.println("초 추가 : " + FishList.get(0).d);// 거리추가
					answer += FishList.get(0).d;
//					System.out.print("잡아먹은 좌표 : " + shark.r + "," + shark.c + " 물고기크기 : " + FishList.get(0).size
//							+ " 상어크기 : " + shark.size
//					);
					
					shark.exp++;
					if (shark.exp == shark.size) {
						//System.out.print(" 잡아먹음");
						shark.exp = 0;
						shark.size++;
					}
//					System.out.print(" -> " + shark.size);
//					System.out.println();
//					System.out.println(answer);
//					System.out.println();
					// 물고기 먹혔으니까 지우기 
					Map[FishList.get(0).r][FishList.get(0).c] = 0;
					FishList.remove(i);
					break;
				} else {
					noEntry = true;
				}
			}
			if (noEntry) break;
			
//			break;
		}
		
		System.out.println(answer);	
	}

	static int dr[] = {1, -1, 0, 0};
	static int dc[] = {0, 0, -1, 1};
	private static int bfs(Fish fish) {
		boolean[][] visited = new boolean[N][N];
		Queue<int[]> queue = new LinkedList<>();
		queue.offer(new int[] {shark.r, shark.c, 0});
		visited[shark.r][shark.c] = true;
		while (!queue.isEmpty()) {
			int[] v = queue.poll();
			int r = v[0];
			int c = v[1];
			int dist = v[2];
			if (r == fish.r && c == fish.c && shark.size > fish.size) return dist; // 먹을 수 있는 경우의 거리만 리턴시킨다.
			for (int d = 0 ; d < 4; d++) {
				int nr = r + dr[d];
				int nc = c + dc[d];
				if (nr < 0 || nc < 0 || nr >= N || nc >= N || visited[nr][nc]) continue;
				if (Map[nr][nc] > shark.size) continue;	// 자신보다 큰 경우는 잡아먹으러 갈 수 없다. // 크기가 같은 경우는 이동가능하다.
				queue.offer(new int[] {nr, nc, dist + 1});
				visited[nr][nc] = true;
			}
		}
		return Integer.MAX_VALUE;
	}



}
