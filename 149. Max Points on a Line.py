class Solution:
    import math
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)<=2:
            return len(points)
        else:
            container={}
            #container={[slope,intercept]:count}
            for m in range(len(points)-1):
                p1=points[m]

                for n in range(m+1,len(points)):
                    p2=points[n]
                    slope=0
                    intercept=0

                    dx=(p2[0]-p1[0])
                    dy=(p2[1]-p1[1])
                    if dx==0:
                        slope= 'inf'
                        intercept= p2[0]

                    elif dy==0:
                        intercept= p2[1]
                    
                    else:
                        slope= dy/dx
                        intercept= float(((p2[1]*dx)-(dy*p2[0]))/dx)
                        if intercept==(-0.0):
                            intercept=0.0
                        
                    item=f'{slope} {intercept}'
                    if item in container:
                        container[item] += 1
                    else:
                        container[item] = 1

            pairs= 8*(max(container.values()))
            alpha= (1+(math.sqrt(1+pairs)))//2
            return int(alpha)
