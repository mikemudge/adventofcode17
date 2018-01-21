from math import sqrt

class Vector(object):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        self.length = abs(x) + abs(y) + abs(z)

    @classmethod
    def parse_from_string(self, str_data):
        x, y, z = map(int, str_data.split(','))
        return Vector(x, y, z)

    def __repr__(self):
        return '<%d, %d, %d>' % (self.x, self.y, self.z)

class Particle(object):

    def __init__(self, str_data):
        p, v, a = str_data.split(', ')
        self.p = Vector.parse_from_string(p[3:-1])
        self.v = Vector.parse_from_string(v[3:-1])
        self.a = Vector.parse_from_string(a[3:-1])

    def __repr__(self):
        return 'p=%s, v=%s, a=%s' % (self.p, self.v, self.a)

    def calculate_v_offset(self):
        # If the acceleration sign differs from the velocity then the v is a handicap, not an asset.
        init_v1 = 0
        if self.a.x > 0:
            init_v1 += self.v.x
        elif self.a.x == 0:
            init_v1 += abs(self.v.x)
        else:
            init_v1 -= self.v.x

        if self.a.y > 0:
            init_v1 += self.v.y
        elif self.a.y == 0:
            init_v1 += abs(self.v.y)
        else:
            init_v1 -= self.v.y

        if self.a.z > 0:
            init_v1 += self.v.z
        elif self.a.z == 0:
            init_v1 += abs(self.v.z)
        else:
            init_v1 -= self.v.z

        return init_v1

    def location_at_time(self, t):

        # Normal motion equations don't apply because we update on ticks.
        # Instead of t**2 we use t * (t + 1) which seems to work.
        # x0 + v0 * t + 1/2 * a * t * (t + 1)
        # x0 + (v0 + 1/2 * a) * t + 1/2 * a * t * t

        return Vector(
            self.p.x + self.v.x * t + self.a.x / 2.0 * (t + 1) * t,
            self.p.y + self.v.y * t + self.a.y / 2.0 * (t + 1) * t,
            self.p.z + self.v.z * t + self.a.z / 2.0 * (t + 1) * t,
        )

    def collides_at_time(self, part):

        a = (self.a.x - part.a.x) / 2.0
        b = (self.v.x - part.v.x) + a
        c = (self.p.x - part.p.x)

        x_times = self.find_times(a, b, c, part)

        # # Try with y instead?
        # a = (self.a.y - part.a.y) / 2.0
        # b = (self.v.y - part.v.y) + a
        # c = (self.p.y - part.p.y)

        # y_times = self.find_times(a, b, c, part)

        # # Try with z instead?
        # a = (self.a.z - part.a.z) / 2.0
        # b = (self.v.z - part.v.z) + a
        # c = (self.p.z - part.p.z)

        # z_times = self.find_times(a, b, c, part)

        # if x_times or y_times or z_times:
        #     print 'x, y, z times=', x_times, y_times, z_times

        for t in x_times:
            p1 = self.location_at_time(t)
            p2 = part.location_at_time(t)

            if p1.x == p2.x and p1.y == p2.y and p1.z == p2.z:
                # print 'particles collide at t=', t
                return t

        return None

    def find_times(self, a, b, c, part):
        times = []
        if a != 0:
            times = solve_quadratic(a, b, c)
        elif b != 0:
            # Its just linear.
            t = solve_linear(b, c)
            if t:
                times = [t]
        else:
            # On the exact same velocity too?
            if c == 0:
                # The particles are on the exact same x for all t's
                # TODO should use y or z to find a valid t?
                print 'part1', self
                print 'part2', part
                raise Exception('Same acceleration, velocity and position')

            # The particles remain a fixed distance apart for all t's (can never collide)
            return []
        return times

def solve_linear(b, c):
    if b == 0:
        raise Exception('Not linear, no gradient')

    # Linear equation is y = mx + b
    # x = vx1 * t + px1
    # x = vx2 * t + px2
    # (vx1 - vx2) * t = px2 - px1
    # b * t = -c
    # t = -c / b

    t = -c / b
    # Non int or negative times are invalid.
    if -c % b == 0 and t >= 0:
        return int(t)
    return None

def solve_quadratic(a, b, c):
    # x = (-b +- sqrt(b ^ 2 - 4ac)) / (2 * a)

    if a == 0:
        raise Exception('Not a quadratic')

    tmp = b ** 2 - 4 * a * c
    if tmp < 0:
        # No possible collisions as sqrt of negative isn't possible.
        # That means there is no point of interception.
        return []
    a2 = (2 * a)
    tmp = sqrt(tmp)

    opts = []
    # Non int or negative are invalid.
    t1 = (-b + tmp) / a2
    if (-b + tmp) % a2 == 0 and t1 >= 0:
        opts.append(int(t1))
    t2 = (-b - tmp) / a2
    if (-b - tmp) % a2 == 0 and t2 >= 0:
        opts.append(int(t2))

    # Return all the possible t's
    return opts

def main():

    with open('input') as f:
        lines = f.readlines()

        min_a = -1
        min_v = -1
        idx = -1
        particles = []
        for i, line in enumerate(lines):
            if line != lines[len(lines) - 1]:
                line = line[:-1]

            particle = Particle(line)
            particles.append(particle)

            # Make a particle object?
            if min_a < 0 or particle.a.length < min_a:
                min_a = particle.a.length
                min_v = particle.calculate_v_offset()
                idx = i
            elif min_a == particle.a.length:
                init_v = particle.calculate_v_offset()
                if init_v < min_v:
                    # They have the same result acceleration but less speed offset initially will put this closer to 0,0,0 in the end.
                    idx = i
                    min_v = init_v
                elif min_v == init_v:
                    raise Exception('Got to use distances too?')

        print 'Part 1:', idx, min_a, min_v

        # Part 2, detect collisions.
        count = 0
        print 'There are %s particles' % len(particles)
        for i, particle in enumerate(particles):
            collides = []
            for ii, p2 in enumerate(particles):
                # Skip matching the exact same particle.
                if particle == p2:
                    continue
                t = particle.collides_at_time(p2)
                if t:
                    collides.append([ii, t])

            if i < 40:
                print 'Particle', i, 'Collides at', ','.join([str(a[1]) + '-' + str(a[0]) for a in collides])
            # print 'Loc 1', particle.location_at_time(t)
            # print 'Loc 2', p2.location_at_time(t)
            if not collides:
                count += 1

        # This count does not account for particles which collide with another particle incorrectly after already having collided earlier.
        # E.g a particle which collides at t=5 should not collide with any other particles at t>5.
        # This input does not appear to have any of those cases.
        print 'Part 2:', count


main()
