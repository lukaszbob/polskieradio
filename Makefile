TARGETS=radio program_name

all: $(TARGETS)

$(TARGETS): %:%.src
	./compile.py $< $@

rebuild: clean all

clean:
	rm -f *~
	rm -f $(TARGETS)
