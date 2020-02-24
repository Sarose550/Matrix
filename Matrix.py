import math
fout = open("pic.ppm","w")
size = 500
fout.write("P3\n"+str(size)+" "+str(size)+"\n255\n")


pixels = []
for i in range(size):
    pixels.append([])
    for j in range(size):
        pixels[i].append([0,0,0])

def print_matrix(matrix):
    x = str()
    y = str()
    z = str()
    one = str()
    for li in matrix:
        x += str(li[0]) + " "
        y += str(li[1]) + " "
        z += str(li[2]) + " "
        one += str(li[3]) + " "
    print(x)
    print(y)
    print(z)
    print(one)

def ident(matrix):
    a = 0
    while a < len(matrix):
        b = 0
        while b < len(matrix):
            if (a == b):
                matrix[a][b] = 1
            else:
                matrix[a][b] = 0
            b += 1
        a += 1

def add_const(m, c):
        for i in range(len(m)):
            for j in range(len(m[i])):
                m[i][j] += c


def matrix_mult(m1, m2):
    copy = new_matrix(len(m2[0]), len(m2))
    e = 0
    while e < len(m2):
        a = 0
        while a < len(m1[0]):
            sum = 0
            b = 0
            while b < len(m1):
                sum += m1[b][a] * m2[e][b]
                b += 1
            copy[e][a] = sum
            a += 1
        e += 1
    c = 0
    while c < len(m2):
        d = 0
        while d < len(m2[0]):
            m2[c][d] = copy[c][d]
            d += 1
        c += 1

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

def scale_matrix(m, c):
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = m[i][j] * c


def draw_lines( matrix, screen, r, g, b):
    for i in range(0,len(matrix),2):
        draw_line(matrix[i][0], matrix[i][1], matrix[i + 1][0], matrix[i + 1][1], pixels, r, g, b)

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0, y0, z0)
    add_point(matrix, x1, y1, z1)

def add_point( matrix, x, y, z=0 ):
    matrix.append([x, y, z, 1])



##########################################################################
#show of matricies and shown on website

print("Testing Add Edge: Adding (0, 69, 420), (4, 5, 6) m2 =")
m2 = new_matrix(4, 0)
add_edge(m2, 0, 69, 420, 4, 5, 6)
print_matrix(m2)
print("\n")
print("Testing Scaling By 3:")
scale_matrix(m2, 3)
print_matrix(m2)
print("\n")
print("Testing Identity m1 =")
m1 = new_matrix(4, 4)
ident(m1)
print_matrix(m1)
print("\n")
print("Testing Matrix mult. m1 * m2 =")
matrix_mult(m1, m2)
print_matrix(m2)
print("\n")
print("Testing Matrix mult. m1 =")
del m1[:]
add_edge(m1, 9, 8, 7, 6, 5, 4)
add_point(m1, 3, 2, 1)
add_point(m1, 0, 9, 8)
print_matrix(m1)
print("\n")
print("Testing Matrix mult. m1 * m2 =")
matrix_mult(m1, m2)
print_matrix(m2)
print("\n")



def draw_line(x0, y0, x1, y1, screen, r, g, b):
	#print("Drawing line from (" + str(x0) + ", " + str(y0) + ") to (" + str(x1) + ", " + str(y1) + ") with RGB " + str(r) + " " + str(g) + " " + str(b))
	if(x0 > x1): #octants 3 through 6
		draw_line(x1, y1, x0, y0, screen, r, g, b)
		return
	if(x0 == x1 and y0 > y1):
		draw_line(x1, y1, x0, y0, screen, r, g, b)
		return
	if(y1 - y0 <= x1 - x0 and y1 - y0 >= 0): #octant 1
		x = x0
		y = y0
		A = y1 - y0
		B = x0 - x1
		d = 2*A + B
		while(x <= x1):
			#print("Plotting (" + str(x) + ", " + str(y) + ")")
			plot(screen, r, g, b, x, y)
			if(d > 0):
				y += 1
				d += 2*B
			x += 1
			d += 2*A
			#print(x, y, d)
	elif(y1 - y0 >= x1 - x0): #octant 2
		x = y0
		y = x0
		A = x1 - x0
		B = y0 - y1
		d = 2*A + B
		while(x <= y1):
			#print("Plotting (" + str(y) + ", " + str(x) + ")")
			plot(screen, r, g, b, y, x)
			if(d > 0):
				y += 1
				d += 2*B
			x += 1
			d += 2*A
	elif(y1 - y0 <= x1 - x0 and y1 - y0 < 0): #octant 8
		x = x0
		y = y1
		A = y0 - y1
		B = x0 - x1
		d = 2*A + B
		while(x <= x1):
			#print("Plotting (" + str(x) + ", " + str(-1 * y) + ")")
			plot(screen, r, g, b, x, y0+y1-y)
			if(d > 0):
				y += 1
				d += 2*B
			x += 1
			d += 2*A
	elif(y1 - y0 < x0 - x1): #octant 7
		x = -1*y0
		y = x0
		A = x1 - x0
		B = y1 - y0
		d = 2*A + B
		while(x <= -1*y1):
			#print("Plotting (" + str(-1*y) + ", " + str(x) + ")")
			plot(screen, r, g, b, y, x)
			if(d > 0):
				y += 1
				d += 2*B
			x += 1
			d += 2*A

def draw_line( x0, y0, x1, y1, screen, r, g, b):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1 and 8
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:            
            d = A + B/2

            while x < x1:
                plot(screen, r, g, b, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, r, g, b, x1, y1)
        #end octant 1

        #octant 8
        else:
            d = A - B/2

            while x < x1:
                plot(screen, r, g, b, x, y)
                if d < 0:
                    y-= 1
                    d-= B
                x+= 1
                d+= A
            #end octant 8 while
            plot(screen, r, g, b, x1, y1)
        #end octant 8
    #end octants 1 and 8

    #octants 2 and 7
    else:
        #octant 2
        if A > 0:
            d = A/2 + B

            while y < y1:
                plot(screen, r, g, b, x, y)
                if d < 0:
                    x+= 1
                    d+= A
                y+= 1
                d+= B
            #end octant 2 while
            plot(screen, r, g, b, x1, y1)
        #end octant 2

        #octant 7
        else:
            d = A/2 - B;

            while y > y1:
                plot(screen, r, g, b, x, y)
                if d > 0:
                    x+= 1
                    d+= A
                y-= 1
                d-= B
            #end octant 7 while
            plot(screen, r, g, b, x1, y1)

def plot(screen, r, g, b, x, y):
	if(x < 0):
		plot(screen, r, g, b, 0, y)
		return
	if(x > 499):
		plot(screen, r, g, b, 499, y)
		return
	if(y < 0):
		plot(screen, r, g, b, x, 0)
		return
	if(y > 499):
		plot(screen, r, g, b, x, 499)
		return
	screen[499 - y][x][0] = r
	screen[499 - y][x][1] = g
	screen[499 - y][x][2] = b

XRES = 500
YRES = 500

#draw_line(0, 0, XRES-1, YRES-1, pixels, 0, 255, 0)
#draw_line(0, 0, XRES-1, YRES // 2, pixels, 0, 255, 0) 
#draw_line(XRES-1, YRES-1, 0, YRES // 2, pixels, 0, 255, 0)

#octants 8 and 4
#draw_line(0, YRES-1, XRES-1, 0, pixels, 0, 0, 255) 
#draw_line(0, YRES-1, XRES-1, YRES//2, pixels, 0, 0, 255)
#draw_line(XRES-1, 0, 0, YRES//2, pixels, 0, 0, 255)

#octants 2 and 6
#draw_line(0, 0, XRES//2, YRES-1, pixels, 255, 0, 0)
#draw_line(XRES-1, YRES-1, XRES//2, 0, pixels, 255, 0, 0)

#octants 7 and 3
#draw_line(0, YRES-1, XRES//2, 0, pixels, 255, 0, 255)
#draw_line(XRES-1, 0, XRES//2, YRES-1, pixels, 255, 0, 255)

#horizontal and vertical
#draw_line(0, YRES//2, XRES-1, YRES//2, pixels, 255, 255, 0)
#draw_line(XRES//2, 0, XRES//2, YRES-1, pixels, 255, 255, 0)

class Turtle:

	def __init__(self, myscreen, x0=XRES//2, y0=YRES//2, head=0, R=0, G=0, B=0):
		self.x = x0
		self.y = y0
		self.heading = head
		self.screen = myscreen
		self.r=R
		self.g=G
		self.b=B
		self.pendown = False
		self.stepcount = 0

	def pd(self):
		self.pendown = not(self.pendown)

	def setcolor(self, newr, newg, newb):
		self.r = newr
		self.g = newg
		self.b = newb

	def fd(self, length):
		newx = (self.x + length * math.sin(math.pi * self.heading / 180))
		newy = (self.y + length * math.cos(math.pi * self.heading / 180))
		intx = (int) (self.x + length * math.sin(math.pi * self.heading / 180))
		inty = (int) (self.y + length * math.cos(math.pi * self.heading / 180))
		goodx = (int) (self.x + 0.0)
		goody = (int) (self.y + 0.0)
		#print("Moving from (" + str(self.x) + ", " + str(self.y) + ") to (" + str(newx) + ", " + str(newy) + ")")
		if(self.pendown):
			draw_line(goodx, goody, intx, inty, self.screen, self.r, self.g, self.b)
		self.x = newx
		self.y = newy

	def setxy(self, newx, newy):
		self.x = newx
		self.y = newy

	def rt(self, angle):
		self.heading += angle

	def lt(self, angle):
		self.heading -= angle

	def movea(self, depth, initialdepth, sidelength):
		if(depth == 0):
			return
		else:
			self.lt(90)
			self.moveb(depth - 1, initialdepth, sidelength)
			self.fd(sidelength)
			self.stepcount += 1
			self.adjustcolor(self.stepcount, initialdepth)
			self.rt(90)
			self.movea(depth - 1, initialdepth, sidelength)
			self.fd(sidelength)
			self.stepcount += 1
			self.adjustcolor(self.stepcount, initialdepth)
			self.movea(depth - 1, initialdepth, sidelength)
			self.rt(90)
			self.fd(sidelength)
			self.stepcount += 1
			self.adjustcolor(self.stepcount, initialdepth)
			self.moveb(depth - 1, initialdepth, sidelength)
			self.lt(90)

	def moveb(self, depth, initialdepth, sidelength):
		if(depth == 0):
			return
		else:
			self.rt(90)
			self.movea(depth - 1, initialdepth, sidelength)
			self.fd(sidelength)
			self.stepcount += 1
			self.adjustcolor(self.stepcount, initialdepth)
			self.lt(90)
			self.moveb(depth - 1, initialdepth, sidelength)
			self.fd(sidelength)
			self.stepcount += 1
			self.adjustcolor(self.stepcount, initialdepth)
			self.moveb(depth - 1, initialdepth, sidelength)
			self.lt(90)
			self.fd(sidelength)
			self.stepcount += 1
			self.adjustcolor(self.stepcount, initialdepth)
			self.movea(depth - 1, initialdepth, sidelength)
			self.rt(90)

	def adjustcolor(self, stepcount, depth):
		totalsteps = 4**depth - 1
		self.r = (int)(128 * math.sin(2 * stepcount * math.pi / totalsteps) + 128)
		self.g = (int)(128 * math.sin(-1 * 2 * math.pi / 3 + 2 * stepcount * math.pi / totalsteps) + 128)
		self.b = (int)(128 * math.sin(-2 * 2 * math.pi / 3 + 2 * stepcount * math.pi / totalsteps) + 128)
		#print("RGB is " + str(self.r) + " " + str(self.g) + " " + str(self.b))

def hilbert(depth, screen):
	    gustavo = Turtle(pixels, 0, 0, 0, 0, 0)
	    sidelength = XRES / 2**depth
	    gustavo.adjustcolor(0, depth)
	    gustavo.fd(sidelength / 2)
	    gustavo.rt(90)
	    gustavo.fd(sidelength / 2)
	    gustavo.pd()
	    gustavo.movea(depth, depth, sidelength)

#hilbert(4, pixels)
matrix = new_matrix()
add_edge(matrix, 3, 3, 3, -3, 3, 3)
add_edge(matrix, -3, 3, 3, -3, -3, 3)
add_edge(matrix, -3, -3, 3, 3, -3, 3)
add_edge(matrix, 3, -3, 3, 3, 3, 3)

add_edge(matrix, 3, 3, -3, -3, 3, -3)
add_edge(matrix, -3, 3, -3, -3, -3, -3)
add_edge(matrix, -3, -3, -3, 3, -3, -3)
add_edge(matrix, 3, -3, -3, 3, 3, -3)

add_edge(matrix, 3, 3, 3, 3, 3, -3)
add_edge(matrix, -3, 3, 3, -3, 3, -3)
add_edge(matrix, -3, -3, 3, -3, -3, -3)
add_edge(matrix, 3, -3, 3, 3, -3, -3)

add_edge(matrix, 1, 1, 1, -1, 1, 1)
add_edge(matrix, -1, 1, 1, -1, -1, 1)
add_edge(matrix, -1, -1, 1, 1, -1, 1)
add_edge(matrix, 1, -1, 1, 1, 1, 1)

add_edge(matrix, 1, 1, -1, -1, 1, -1)
add_edge(matrix, -1, 1, -1, -1, -1, -1)
add_edge(matrix, -1, -1, -1, 1, -1, -1)
add_edge(matrix, 1, -1, -1, 1, 1, -1)

add_edge(matrix, 1, 1, 1, 1, 1, -1)
add_edge(matrix, -1, 1, 1, -1, 1, -1)
add_edge(matrix, -1, -1, 1, -1, -1, -1)
add_edge(matrix, 1, -1, 1, 1, -1, -1)

add_edge(matrix, 3, 3, 3, -1, 1, 1)
add_edge(matrix, -3, 3, 3, -1, -1, 1)
add_edge(matrix, -3, -3, 3, 1, -1, 1)
add_edge(matrix, 3, -3, 3, 1, 1, 1)
add_edge(matrix, 3, 3, -3, -1, 1, -1)
add_edge(matrix, -3, 3, -3, -1, -1, -1)
add_edge(matrix, -3, -3, -3, 1, -1, -1)
add_edge(matrix, 3, -3, -3, 1, 1, -1)

#shoulda for-looped this :(

scale_matrix(matrix, 30)
add_const(matrix, 250)


#print(screen)

draw_lines( matrix, pixels, 0, 255, 0)

for i in range(size):
    for j in range(size):
        fout.write(str(pixels[i][j][0])+" "+str(pixels[i][j][1])+" "+str(pixels[i][j][2])+" ")

    fout.write("\n")
